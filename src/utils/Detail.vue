<template>
    <div v-show="showDetails">
        <transition name="detail">
            <div class="detail-mask">
                <div class="detail-wrapper">
                    <div class="detail-container" @click="" v-show="showContent && actionType == 'show'">
                        <div class="detail-header">
                            详细信息
                        </div>
                        <div class="detail-body">
                            <table>
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td>{{value}}</td>
                                        <td>{{detailContent[key]}}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="detail-footer">
                            <center>
                            <button class="ui primary button" @click="$emit('close')">
                                OK
                            </button>
                            <button class="ui button" @click="modifier">
                                修改
                            </button>
                            </center>
                        </div>
                    </div>
                    <div class="detail-container modifier" @click="" v-show="!showContent || actionType == 'create'">
                        <div class="detail-header" v-show="actionType == 'show'">
                            修改
                        </div>
                        <div class="detail-header" v-show="actionType == 'create'">
                            新建
                        </div>
                        <div class="detail-body">
                            <table>
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td>{{value}}</td>
                                        <td>
                                            <input v-model=newContent[key]>
                                            </input>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="detail-footer">
                            <center>
                            <button class="ui red button" @click="closeModifier">
                                放弃
                            </button>
                            <button class="ui primary button" @click="realModify" v-show="actionType == 'show'">
                                修改
                            </button>
                            <button class="ui primary button" @click="realModify" v-show="actionType == 'create'">
                                新建
                            </button>
                            </center>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
        <div v-show=debug>
            <p> -----------Detail debug below----------- </p>
            <p> showDetails : {{showDetails}} </p>
            <p> detailTitle : {{detailTitle}} </p>
            <p> detailContent : {{detailContent}} </p>
            <p> actionType : {{actionType}} </p>
        </div>
    </div>
</template>

<script>
export default {
    props : ['showDetails', 'detailTitle', 'detailContent', 'actionType', 'savecb', 'updatecb', 'removecb'],
    data: function() {
        return {
            debug : true,
            newContent : {},
            showContent : true,
        }
    },
    methods : {
        modifier: function(){
            this.newContent = this.deepCopy(this.detailContent)
            this.showContent = false
        },
        closeModifier(){
            this.newContent = {}
            this.showContent = true
            if (this.actionType == 'create'){
                this.$emit('close')
            }
            
        },
        realModify(){
            console.log("!!!!", this.cmp(this.newContent, this.detailContent))
            if (this.cmp(this.newContent, this.detailContent)){
                this.$store.dispatch('showMsg', '无修改', 'info')
                this.closeModifier()
            }else{
                this.showContent = true
                if (this.actionType == 'create'){
                    this.savecb(this.newContent)
                    this.closeModifier()
                }else if(this.actionType == 'show'){
                    this.updatecb(this.newContent)
                }else{
                    console.log('error actionType', this.actionType)
                }
            }
        },
        deepCopy : function(source) { 
            var result={};
            for (var key in source) {
                result[key] = typeof source[key] === 'object' ? deepCoyp(source[key]): source[key];
            } 
            return result; 
        },
        cmp : function( x, y ) {  
            // If both x and y are null or undefined and exactly the same  
            if ( x === y ) {  
                return true;  
            }  

            // If they are not strictly equal, they both need to be Objects  
            if ( ! ( x instanceof Object ) || ! ( y instanceof Object ) ) {  
                return false;  
            }  

            // They must have the exact same prototype chain, the closest we can do is  
            // test the constructor.  
            if ( x.constructor !== y.constructor ) {  
                return false;  
            }  

            for ( var p in x ) {  
                // Inherited properties were tested using x.constructor === y.constructor  
                if ( x.hasOwnProperty( p ) ) {  
                    // Allows comparing x[ p ] and y[ p ] when set to undefined  
                    if ( ! y.hasOwnProperty( p ) ) {  
                        return false;  
                    }  

                    // If they have the same strict value or identity then they are equal  
                    if ( x[ p ] === y[ p ] ) {  
                        continue;  
                    }  

                    // Numbers, Strings, Functions, Booleans must be strictly equal  
                    if ( typeof( x[ p ] ) !== "object" ) {  
                        return false;  
                    }  

                    // Objects and Arrays must be tested recursively  
                    if ( ! Object.equals( x[ p ],  y[ p ] ) ) {  
                        return false;  
                    }  
                }  
            }  

            for ( p in y ) {  
                // allows x[ p ] to be set to undefined  
                if ( y.hasOwnProperty( p ) && ! x.hasOwnProperty( p ) ) {  
                    return false;  
                }  
            }  
            return true;  
        }  
    }

}
</script>

<style>
table {
  width: 90%;
  overflow: scroll;
  margin-left:auto;
  margin-right:auto;
}
td{
    width: 50%;
}
.detail-mask{
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
.detail-wrapper {
  display: table-cell;
  vertical-align: middle;
  z-index: 6000;
  overflow: scroll;
}

.detail-container {
  width: 75%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  height:90%;
  overflow: scroll;
}
.modifier {
    z-index: 6050;
}

.detail-header h3 {
    margin-top: 0;
    color: #42b983;
}

.detail-body {
    margin: 20px 0;
}

.detail-footer {
}
.detail-default-button{
    float: right;
}

.detail-enter{
  opacity: 0;
}
.detail-leave-to{
  opacity: 0;
}
.modal-enter .modal-contailner,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}


</style>

