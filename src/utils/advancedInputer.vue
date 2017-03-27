<template>
    <div>
        <span>
            <div v-if="header.immutable">
                immutable
            </div>
            <div v-else-if="header.type==='option'" class="ui compact menu">
                <div class="ui simple dropdown item">{{currentValue}}<i class="dropdown icon"></i>
                    <div class=menu>
                        <div v-for="op in header.selectOptions" class=item @click="setOption(op)">{{op}}</div>
                    </div>
                </div>
            </div>
            <div v-else-if="header.type==='date'">
                <Date-picker type="date" placeholder="选择日期" style="width: 200px"></Date-picker>
            </div>
            <div v-else>
                <input v-model=currentValue class='ui input'>
                </input>
            </div>
            {{header}}
            {{currentValue}}
        </span>
    </div>
</template>

<script>
//import DatePicker from '../../node_modules/iview/src/components/date-picker';
export default {
    data: function() {
        return {
            currentValue: this.value
        }
    },
    props : ['value', 'header'],
    watch : {
        value : function(x){
            this.currentValue = x
        }
    },
    methods : {
        setOption(op){
            this.currentValue = op
            this.$emit('input', this.currentValue)
        }
    }

}
</script>

<style>
</style>

