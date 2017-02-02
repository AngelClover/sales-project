<template>
    <div v-show="showDetails">
        <transition name="detail">
            <div class="detail-mask">
                <div class="detail-wrapper">
                    <div class="detail-container" @click="">
                        <div class="detail-header">
                            default header
                            
                        </div>
                        <div class="detail-body">
                            <table>
                                <tbody>
                                    <tr v-for="(value, key) in detailTitle">
                                        <td>{{value.name}}</td>
                                        <td>{{detailContent[key]}}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="detail-footer">
                            <button class="modal-default-button" @click="$emit('close')">
                                OK
                            </button>
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
    props : ['showDetails', 'detailTitle', 'detailContent', 'actionType'],
    data: function() {
        return {
            debug : true
        }
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
}
.detail-wrapper {
  display: table-cell;
  vertical-align: middle;
  z-index: 6000;
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

