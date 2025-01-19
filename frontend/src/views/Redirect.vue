<template>
    <div class="text-3xl flex flex-col justify-center items-center space-y-2 font-bold text-center my-16">
        <div class="animate-pulse">Redirected...</div>
        <div class="text-xl text-red-500">If not redirected, please click here</div>
        <a class="hover:text-blue-700 hover:underline text-lg" :href="long_url">{{ long_url }}</a>
    </div>
</template>
<script>
import axios from 'axios';
export default{
    data(){
        return{
            shortCode: this.$route.params.shortCode,
            long_url: ""
        }
    },
    created(){
        this.get_long_url()
    },
    methods: {
        get_long_url(){
            if(this.shortCode === "" || this.shortCode === null){
                alert("Short code not valid")
                return
            }

            axios.get("http://127.0.0.1:5000/shorten/" + this.shortCode)
            .then(response => {
                if(response.status === 200){
                    this.long_url = response.data.url
                }
            })
            .catch(error => {
                if(error.status === 400){
                    alert(error.response.data.error)
                }
            })
            .finally(() => {
                window.location.href = this.long_url
            })
        },
    }
}
</script>