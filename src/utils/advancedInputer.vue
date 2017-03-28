<template>
    <div>
        <span>
            <div v-if="header.immutable">
                <label>{{currentValue}}</label>
            </div>
            <div v-else-if="header.type==='option'" class="ui compact menu">
                <div class="ui simple dropdown item">{{currentValue}}<i class="dropdown icon"></i>
                    <div class=menu>
                        <div v-for="op in header.selectOptions" class=item @click="setOption(op)">{{op}}</div>
                    </div>
                </div>
            </div>
            <div v-else-if="header.type==='date'">
                <Date-picker type="date" placeholder="选择日期" style="width: 200px" v-model=currentDate @on-change="setDate"></Date-picker>
            </div>
            <div v-else-if="header.type==='time'">
                <Date-picker type="datetime" placeholder="选择日期和时间" style="width: 200px" v-model=currentDate @on-change="setDatetime"></Date-picker>
            </div>
            <div v-else-if="header.type==='number'">
                <Input-number v-model="currentValue"></Input-number>
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
            currentValue: this.value,
            currentDate: this.header && this.header.type === 'date' && this.value && new Date(Date.parse(this.value.replace(/-/g,  "/"))) || new Date()
        }
    },
    props : ['value', 'header'],
    watch : {
        value : function(x){
            if (x){
                console.log('watch value various -> ', x)
                this.currentValue = x
                if (this.header && this.header.type === 'date'){
                    this.currentDate = new Date(Date.parse(x.replace(/-/g, "/")));
                    console.log('x:', x, '-> now:', this.currentDate)
                }
            }
        }
    },
    methods : {
        setOption(op){
            this.currentValue = op
            this.$emit('input', this.currentValue)
        },
        setDate(){
            var x = (this.currentDate.getYear() + 1900) + '-' + (this.currentDate.getMonth() + 1) + '-' + this.currentDate.getDate()
            console.log('emit input date', this.currentDate, " -> ", x)
            this.$emit('input', x)
        },
        setDatetime(){
            var x = (this.currentDate.getYear() + 1900) + '-' + (this.currentDate.getMonth() + 1) + '-' + this.currentDate.getDate()
            x += " " + this.currentDate.getHours() + ":" + this.currentDate.getMinutes() + ":" + this.currentDate.getSeconds()
            console.log('emit input datetime', this.currentDate, " -> ", x)
            this.$emit('input', x)
        }
    }

}
</script>

<style>
</style>

