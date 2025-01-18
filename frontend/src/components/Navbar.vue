<template>
    <nav class="bg-gray-900 text-gray-200 shadow-md">
        <div class="container mx-auto flex items-center justify-between py-2 px-4">
            <!-- Menú lateral estilo Linux -->
            <div class="flex items-center space-x-4">
                <!-- Nombre del sistema -->
                <div class="text-xl font-bold">
                    <a href="/" class="hover:text-gray-400">Short URL</a>
                </div>
            </div>
    
            <!-- Menú centrado -->
            <ul class="hidden md:flex space-x-6">
                <li>
                    <router-link to="/" class="hover:text-gray-400">Inicio</router-link>
                </li>
                <li>
                    <a href="#" class="hover:text-gray-400">Docs</a>
                </li>
                <li>
                    <router-link to="/about" class="hover:text-gray-400">About</router-link>
                </li>
            </ul>
    
            <!-- Botones de acciones -->
            <div class="flex items-center space-x-4">
                <!-- Icono de búsqueda -->
                <button
                    class="p-2 rounded hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    class="w-6 h-6"
                    >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M11 19a8 8 0 100-16 8 8 0 000 16zm10 2l-4-4"
                    />
                    </svg>
                </button>
            </div>
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
  