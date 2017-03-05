<template>
    <div v-if=showAuthDetail>
            <transition name="detail">
            <div class="detail-mask">
                <div class="detail-wrapper">
                    <div class="detail-container">
                        <div class="detail-header">
                            {{detailContent.username || detailContent.email || detailContent.nickname}}的权限
                        </div>
                        <div class="detail-body">
                            <table border="0">
                                <tr>
                                    <th>Header</th>
                                    <th>读</th>
                                    <th>写</th>
                                    <th>审批</th>
                                </tr>
                                <tr v-for="per in perList">
                                    <td>{{per.displayName}}</td>
                                    <td v-for="col in columns" >
                                        <div class="ui test toggle checkbox">
                                            <input type="checkbox"  v-model="detailContent.permission[per.attr][col.attr]">
                                            <label>{{col.displayName}}
                                            </label>
                                        </div>
                                    </td>
                                    <td v-if=debug>
                                        detailContent: {{detailContent.permission[per.attr]}}
                                    </td>
                                </tr>
                            </table>
                        </div>
                        <div class="detail-footer" align=center>
                            <button @click="$emit('close')">
                                ok
                            </button>
                        </div>
                    </div>
                    
                </div>
                
            </div>
            </transition>
    </div>
</template>

<script>
export default {
    props : ['showAuthDetail', 'detailContent', 'perList'],
    data: function() {
        return {
            debug : false,
            columns : [
            {attr:"read", displayName:"读"},
            {attr:"write", displayName:"写"},
            {attr:"approve", displayName:"审"},
            ],
        }
    },
    methods : {
        mounted() {
            $('.ui .checkbox').checkbox()
        },
    }
}
</script>

<style>
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

