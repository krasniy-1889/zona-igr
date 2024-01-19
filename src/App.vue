<script setup lang="ts">
import { ref } from 'vue';
import NavBar from '@/components/NavBar.vue';
interface IUser {
  username: string;
  email: string;
  password: string;
}
const users = ref<IUser[]>([
  {
    username: 'admin',
    email: 'admin',
    password: 'admin',
  },
]);
</script>

<template>
  <NavBar />
  <div class="container">
    <RouterView />
  </div>
</template>
