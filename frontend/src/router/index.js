import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Redirect from '../views/Redirect.vue';

const routes = [{
        path: '/',
        name: 'home',
        component: Home,
    },
    {
        path: '/:shortCode',
        name: 'redirect',
        component: Redirect,
    },
    {
        path: '/about',
        name: 'about',
        component: About,
    }
];

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes,
});

export default router;