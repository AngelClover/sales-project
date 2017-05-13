<template>
    <div>
        <Label>上传文件类型: </Label> 
        <Input v-model=uploadFiletype width=100></Input>
        <br/>
        <uupload :filetype=uploadFiletype :cb=uploadcb>
        </uupload>
        <div v-if="titleKey && titleKey.length > 0 && content && content.length > 0">
            <Table width=760 stripe :columns="titleKey" :data="content">
            </Table>
        </div>
        <div v-if=debug>
            title: {{title}}
            <br/>
            content : {{content}}

        </div>
    </div>
</template>

<script>
import uupload from '../utils/uploader.vue'
export default {
    data: function() {
        return {
            debug : false,
            uploadPrefix : 'http://angelclover.win:8088/uploadfiles/',
            uploadFiletype : "",
            uploadcb : this.fileListRefresh
        }
    },
    components : {
        uupload
    },
    computed : {
        title(){
            return this.$store.getters.uploadfilesTitle
        },
        content(){
            return this.$store.getters.uploadfilesContent
        },
        titleKey(){
            var ret = []
            for (var i in this.title){
                var t = {}
                t.key = this.title[i].item
                t.title = this.title[i].displayName
                t.width = 100
                t.sortable = true

                if (t.key === "filename" || t.key === "displayName") continue
                //why?
                /*
                if (t.key === 'id' || t.title.search('编号') >= 0){
                    t.fixed = 'left'
                }
                */
                ret.push(t)
            }
            ret.push({
                title: '文件预览',
                key: 'displayName',
                fixed: 'right',
                width: 300,
                align: 'center',
                render (row, column, index) {
//                    return row.displayName
                    var ret = ""
                    var uploadPrefix = 'http://angelclover.win:8088/uploadfiles/'
                    ret += '<p><a href=' + uploadPrefix + row.filename + ' target=_blank>' + row.displayName + '</a></p>'
                    return ret;
                }
            })
            ret.push({
                title : '操作',
                key : 'action',
                fixed : 'right',
                width : 80,
                align : 'center',
                render (row, column, index){
                    return `<ToolTip content="删除请慎重"> <i-button type="error" size="small" @click="deleteFile(${index}, ${row.id})">删除</i-button> </ToolTip>`;
                }
            })
            console.log('titleKey', ret)
            return ret
        }
    },
    created(){
        this.$store.dispatch('getFileList', this.$store.getters.getMe)
    },
    methods : {
        mounted(){
            console.log("user", this.$store.getters.getMe)//TODO: is null
            this.$store.dispatch('getFileList', this.$store.getters.getMe)
        },
        deleteFile(index, id){
            console.log('deleteFile', index, id)
                this.$store.dispatch('removeFile', {id:id, userid:this.$store.getters.getMe})
        },
        fileListRefresh(){
            this.$store.dispatch('getFileList', this.$store.getters.getMe)
        }
    }
}
</script>

<style>
</style>

