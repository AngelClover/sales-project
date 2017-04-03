<template>
    <div>
        <span>
            <div v-if="header.immutable" class="input">
                <label>{{currentValue}}</label>
            </div>
            <div v-else-if="header.type==='option'" class="ui compact menu input">
                <div class="ui simple dropdown item">{{currentValue}}<i class="dropdown icon"></i>
                    <div class=menu>
                        <div v-for="op in header.selectOptions" class=item @click="setOption(op)">{{op}}</div>
                    </div>
                </div>
            </div>
            <div v-else-if="header.type==='date'" class="input">
                <Date-picker type="date" placeholder="选择日期" style="width: 200px" v-model=currentDate @on-change="setDate"></Date-picker>
            </div>
            <div v-else-if="header.type==='time'" class="input">
                <Date-picker type="datetime" placeholder="选择日期和时间" style="width: 200px" v-model=currentDate @on-change="setDatetime"></Date-picker>
            </div>
            <div v-else-if="header.type==='number'" class="input">
                <Input-number v-model="currentNumber" @on-change="handleNumber"></Input-number>
            </div>
            <div v-else class="input">
                <Input v-model="currentString" style="width: 300px" @on-change="handleInput">
                </Input>
            </div>
            <div v-if="debug">
            {{header}}
            {{currentValue}}
            </div>
        </span>
    </div>
</template>

<script>
//import DatePicker from '../../node_modules/iview/src/components/date-picker';
export default {
    data: function() {
        return {
            debug : false,
            currentValue: this.value,
            currentDate: this.header && this.header.type === 'date' && this.value && new Date(Date.parse(this.value.replace(/-/g,  "/"))) || new Date(),
            currentString : "",
            currentNumber : 1,
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
        },
        currentValue: function(x){
            console.log('currentValue various =>', x)
            this.$emit('input', x)
        },
        currentNumber: function(x){
            console.log('currentNumber various =>', x)
            this.$emit('input', x)
        },
        currentString: function(x){
            console.log('currentString various =>', x)
            this.$emit('input', x)
        },

    },
    methods : {
        setOption(op){
            this.currentValue = op
            this.$emit('input', this.currentValue)
            console.log('set input option ->', this.currentValue)
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
        },
        handleInput(event){
            //console.log('set input value ->', this.currentValue)
            this.$emit('input', this.currentString)
        },
        handleNumber(event){
            console.log('set input number value ->', this.currentNumber)
            this.$emit('input', this.currentNumber)
        }
    }

}
</script>

<style>
.input{
    margin : 5px
}
</style>

