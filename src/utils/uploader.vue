<template>
    <div>
        <Upload :action=uploadAPI type="drag" :on-success=Succ :on-error=Error :on-remove=fileRemove :on-preview=filePreview :on-progress=Progress :before-upload=before :max-size=fileMaxSize :on-format-error=formatError :on-exceeded-size=sizeError>
        <!--
        <Button type="ghost" icon="ios-cloud-upload-outline">上传文件</Button>
        -->
        <div style="padding: 20px 0">
            <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
            <p>点击或将文件拖拽到这里上传</p>
        </div>
        </Upload>
    </div>
</template>

<script>
export default {
    props : ['value'],
    data: function() {
        return {
            uploadAPI : "http://angelclover.win:9000/" + "api/v1.0/" + "upload",
            fileMaxSize : 10240, //kb
            fileList : [],
        }
    },
    watch : {
        value (x){
            console.log('value in uploader ->', x)
            if (false){
                this.fileList = this.value
            }
        },
        fileList (x){
            console.log('fileList ->', x)
            var ret = []
            for (var i in x){
                if (x[i] && x[i].filename)
                    ret.push(x[i].filename)
            }
            this.$emit('input', ret)
        }
    },
    methods : {
        before(file){
            console.log('before', file)
        },
        Succ(res, file, fileList){
            console.log('succ', res, file, fileList)
            if (res && res.data){
                this.fileList.push({
                    'filename' : res.data.filename,
                    'uid' : file.uid,
                })
            }
        },
        Error(err, response, file){
            console.log('error', err, response, file)
        },
        Progress(e, percent, fileList){
            console.log('progress', e, percent, fileList)
        },
        fileClick(x){
            console.log('click', x)
        },
        filePreview(file){
            console.log('preview', file)
            if (file && file.response && file.response.data && file.response.data.filename){
                var uri = "http://angelclover.win:8088/uploadfiles/" + file.response.data.filename
                window.open(uri)
                //window.location.href(uri) //TODO:bad
            }
        },
        fileRemove(file){
            console.log('remove', file)
            for (var i in this.fileList){
                if (this.fileList[i].uid == file.uid){
                    console.log('remove the ', i, 'th')
                    this.fileList.splice(i, 1)
                }
            }
        },
        formatError(file, fileList){
            console.log('formatError', file, fileList)
            if (file){
                var msg = '文件名' + file.name + '格式有误'
                this.$store.dispatch('showMsg', msg, 'error')
            }
        },
        sizeError(file, fileList){
            console.log('file size error', file, fileList)
            if (file){
                var fileSize = file.size / 1024 / 1024
                var msg = '文件大小为' + fileSize + 'MB, 超出' + this.fileMaxSize / 1024 + 'MB限制'
                this.$store.dispatch('showMsg', msg, 'error')
            }
        },
    }
}
</script>

<style>
</style>

