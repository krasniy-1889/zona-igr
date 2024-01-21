<script lang="ts" setup>
import { useAuthStore } from '@/stores';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const store = useAuthStore();
const router = useRouter();
const username = ref<string>('');
const email = ref<string>('');
const password = ref<string>('');

const register = async () => {
  await store.register(username.value, email.value, password.value);
  await router.push({ name: 'login' });
};
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card mt-5">
          <div class="card-header">Register</div>
          <div class="card-body">
            <form @submit.prevent="register">
              <div class="form-group mb-3">
                <label for="username">Username</label>
                <input
                  v-model="username"
                  type="text"
                  class="form-control"
                  id="username"
                  placeholder="Enter your username"
                />
              </div>
              <div class="form-group mb-3">
                <label for="username">Email</label>
                <input v-model="email" type="email" class="form-control" id="email" placeholder="Enter your email" />
              </div>
              <div class="form-group mb-3">
                <label for="password">Password</label>
                <input
                  v-model="password"
                  type="password"
                  class="form-control"
                  id="password"
                  placeholder="Enter your password"
                />
              </div>
              <button type="submit" class="btn btn-primary">Register</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
