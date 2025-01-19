<template>
    <nav class="bg-gray-900 text-gray-200 shadow-md">
        <div class="container mx-auto flex items-center justify-between py-2 px-4">
            <!-- Menú lateral estilo Linux -->
            <div class="flex items-center space-x-4">
                <!-- Nombre del sistema -->
                <div class="text-xl font-bold">
                    <router-link to="/" class="hover:text-gray-400">Short URL</router-link>
                </div>
            </div>
    
            <!-- Menú centrado -->
            <ul class="hidden md:flex space-x-6">
                <li>
                    <router-link to="/" class="hover:text-gray-400">Home</router-link>
                </li>
                <li>
                    <a href="#" class="hover:text-gray-400">API Docs</a>
                </li>
            </ul>
        </div>
    </nav>
</template>
  
<script>
    export default {
        name: "NavbarLinux",
        data() {
            return {
                menuOpen: false,
            };
        },
        methods: {
            toggleMenu() {
                this.menuOpen = !this.menuOpen;
            },
        },
    };
</script>
  
  <style scoped>
  /* Opcional: Estilo inspirado en interfaces Linux */
  nav {
    font-family: "Roboto", sans-serif;
  }
  </style>
  