<template>
    <div class="mb-4 flex items-center justify-center flex-col space-y-4">
        <div class="py-12 w-full bg-gray-100 flex items-center justify-center flex-col space-y-4">
            <h1 class="text-3xl font-bold">Short URL</h1>
            <transition
                enter-active-class="transition ease-out duration-400"
                enter-from-class="opacity-0 scale-95"
                enter-to-class="opacity-100 scale-100"
                leave-active-class="transition ease-in duration-400"
                leave-from-class="opacity-100 scale-100"
                leave-to-class="opacity-0 scale-95"
            >
                <div v-if="url_shorten === '' && !loading" class="flex">
                    <div class="rounded-l-md border border-black w-96 flex items-center justify-between">
                        <input class="w-full p-4 bg-transparent placeholder:text-gray-800 border-none focus:outline-none" v-model="url" placeholder="Enter the link here" />
                        <button v-if="url != ''" @click="url = ''" type="button" title="Delete button" class="flex items-center justify-center mr-2">
                            <svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm7.707-3.707a1 1 0 0 0-1.414 1.414L10.586 12l-2.293 2.293a1 1 0 1 0 1.414 1.414L12 13.414l2.293 2.293a1 1 0 0 0 1.414-1.414L13.414 12l2.293-2.293a1 1 0 0 0-1.414-1.414L12 10.586 9.707 8.293Z" clip-rule="evenodd"/>
                            </svg>                                      
                        </button>
                    </div>
                    <button type="button" class="px-4 py-2 text-white font-bold rounded-r-md bg-yellow-500 focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400" @click="shortenURL">Shorten URL</button>
                </div>
            </transition>
            <div class="flex flex-row gap-2" v-if="loading">
                <div class="w-4 h-4 rounded-full bg-red-500 animate-bounce"></div>
                <div
                    class="w-4 h-4 rounded-full bg-red-500 animate-bounce [animation-delay:-.3s]"
                ></div>
                <div
                    class="w-4 h-4 rounded-full bg-red-500 animate-bounce [animation-delay:-.5s]"
                ></div>
            </div>
            <transition
                enter-active-class="transition ease-out duration-400"
                enter-from-class="opacity-0 scale-95"
                enter-to-class="opacity-100 scale-100"
                leave-active-class="transition ease-in duration-400"
                leave-from-class="opacity-100 scale-100"
                leave-to-class="opacity-0 scale-95"
            >
                <div v-if="url_shorten !== ''" class="flex flex-col justify-center space-y-4">
                    <div class="flex justify-center">
                        <input type="text" class="p-4 w-96 border border-black rounded-l-md bg-gray-100" v-model="url_shorten" disabled>
                        <button type="button" @click="doCopy()" class="px-4 py-2 text-white font-bold rounded-r-md bg-green-600 focus:ring-2 focus:ring-green-400 focus:border-green-400">Copy URL</button>
                    </div>
                    <div>
                        Long URL: <a class="hover:text-blue-700 hover:underline" :href="url" target="_blank">{{ url }}</a>
                    </div>
                    <div class="flex justify-center">
                        <button type="button" class="p-4 text-white font-bold rounded-md bg-blue-500 focus:ring-2 focus:ring-blue-400 focus:border-blue-400" @click="resetForm">Shorten another URL</button>
                    </div>
                </div>
            </transition>
        </div>
        <div class="text-2xl font-bold">Last links</div>
        <table>
            <thead>
                <tr>
                    <th>Shorten URL</th>
                    <th>Long URL</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="link in links" :key="link.id">
                    <td><a class="hover:text-blue-700 hover:underline" target="_blank" :href="base_url + link.shortCode">{{ base_url + link.shortCode }}</a></td>
                    <td><a class="hover:text-blue-700 hover:underline" target="_blank" :href="link.url">{{ link.url }}</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
    import axios from 'axios'
    import { copyText } from 'vue3-clipboard';

    export default {
        name: 'Home',
        data() {
            return {
                base_url: "https://shortenurl-gamma.vercel.app/",
                links: [],
                url: "",
                url_shorten: "",
                loading: false
            };
        },
        methods: {
            shortenURL(){
                if(this.url === "" || this.url === null){
                    alert("Enter a URL")
                    return
                }

                if (!this.validarURL()) {
                    alert("URL is not valid");
                    return
                }

                this.loading = true
                axios.post("http://127.0.0.1:5000/shorten", {"url": this.url})
                .then(response => {
                    if(response.status === 200){
                        this.url_shorten = this.base_url + response.data.shortCode
                        this.links.unshift(response.data)
                    }
                })
                .catch(error => {
                    if(error.status === 400){
                        alert(error.response.data.error)
                    }
                })
                .finally(() => {
                    this.loading = false
                })
            },
            validarURL() {
                // Usar una expresión regular para validar la URL
                const patron = new RegExp(
                    "^(https?:\\/\\/)" + // http o https
                    "((([a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,})|localhost)" + // Dominio o localhost
                    "(\\:\\d+)?(\\/.*)?$", // Puerto y ruta opcionales
                    "i"
                );
                return patron.test(this.url); // Retorna true si la URL es válida
            },
            resetForm(){
                this.url_shorten = ""
                this.url = ""
            },
            doCopy(){
                let url = this.url_shorten
                copyText(url, undefined, (error, event) => {
                    if (error) {
                        alert("Copy error!")
                        console.log(error)
                    } else {
                        alert("Copiado en portapapeles!")
                    }
                })
            },
        }
    }
</script>