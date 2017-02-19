<template>
    <div v-show="showPref">
        <transition name="prefs">
        <div class='pref-mask'>
            <div class="pref-wrapper">
                <div class="pref-container">
                    <div class="pref-header">
                        偏好设置
                    </div>
                    <div class="pref-body">
                        <div>
                            <div v-for="(item, index) in newPreference" class="ui toggle checkbox">
                                <input type="checkbox" v-model="item['value']" >
                                <label> {{item['displayName']}}</label>
                            </div>
                        </div>



                        <div v-show=debug>
                            title:{{oriTitle}}
                            <br/>
                            newPref:{{newPreference}}
                            <br/>
                            pref:{{preference}}
                        </div>
                    </div>
                    <div class="pref-footer">
                        <center>
                            <button @click="selectAll" class="ui green  button">
                                全选 
                            </button>
                            <button @click="close" class="ui primary button">
                                OK
                            </button>
                        </center>
                    </div>
                </div>
                
            </div>
        </div>
        </transition>
    </div>
</template>

<script>
export default {
    props : ['oriTitle', 'location', 'showPref'],
    data: function() {
        return {
            newPreference : [],
            debug : false
        }
    },
    computed : {
        preference : function(){
            //localStorage.removeItem(this.location)
            var readStr = localStorage.getItem(this.location)
            console.log('readStr', readStr)
            var prefobj = JSON.parse(readStr || "{}") 
            var preference = prefobj["pref"] || []
            var shw = this.showPref
            shw != shw
            console.log('computed pref ', preference.length, Object.values(this.oriTitle).length)
            if (preference.length != Object.values(this.oriTitle).length){
                preference = []
                for (var item in this.oriTitle){
                    var d = {}
                    d['name'] = item
                    d['displayName'] = this.oriTitle[item]
                    d['value'] = true
                    preference.push(d)
                }
            }
            //console.log('computed pref:', preference)
            this.newPreference = preference
            return preference
            return []
        }
    },
    methods : {
        mounted() {
            $('.ui .checkbox').checkbox()
        },
        close(){
            var writeStr = JSON.stringify({"pref":this.newPreference})
            localStorage.setItem(this.location, writeStr)
            console.log('writeStr', writeStr)
            this.$emit('close')
        },
        selectAll(){
            //console.log('selectAll')
            var target = false
            for (var item in this.newPreference){
                if (this.newPreference[item].value == false){
                    target = true
                    break
                }
            }
            for (var item in this.newPreference){
                this.newPreference[item].value = target
            }
        }
    }
}
</script>

<style>
.pref-mask{
  position: fixed;
  z-index: 5000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
  overflow: scroll;
}
.pref-wrapper {
  display: table-cell;
  vertical-align: middle;
  z-index: 6000;
  overflow: scroll;
}

.pref-container {
  width: 40%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  height:60%;
  overflow: scroll;
}
.pref-header h3 {
    margin-top: 0;
    color: #42b983;
}

.pref-body {
    margin: 20px 0;
}

.pref-footer {
}
.pref-default-button{
    float: right;
}


</style>

