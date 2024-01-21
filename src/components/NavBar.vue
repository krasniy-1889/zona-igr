<script lang="ts" setup>
import { useAuthStore } from '@/stores';
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

const store = useAuthStore();
const { isAuth, authUser } = storeToRefs(useAuthStore());
const router = useRouter();

const logout = async () => {
  store.logout();
  await router.push({ name: 'login' });
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-sm bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'home' }">Zona Igr</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link :to="{ name: 'posts' }" class="nav-link active" aria-current="page" href="#"
                >Posts</router-link
              >
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                {{ isAuth ? authUser!.username : 'Гость' }}
              </a>
              <ul class="dropdown-menu">
                <div v-if="!isAuth">
                  <li><router-link :to="{ name: 'login' }" class="dropdown-item">Login</router-link></li>
                  <li><router-link :to="{ name: 'register' }" class="dropdown-item">Register</router-link></li>
                </div>
                <div v-if="isAuth">
                  <form @submit.prevent="logout">
                    <li><button type="submit" href="#" class="dropdown-item" @click="logout">Logout</button></li>
                  </form>
                </div>
              </ul>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  </header>
</template>

<style lang="scss"></style>
