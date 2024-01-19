<script lang="ts" setup>
import { useAuthStore } from '@/stores';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const store = useAuthStore();
const router = useRouter();
const username = ref<string>('');
const password = ref<string>('');

const login = async () => {
  await store.login(username.value, password.value);
  await router.push({ name: 'home' });
};
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card mt-5">
          <div class="card-header">Login</div>
          <div class="card-body">
            <form @submit.prevent="login">
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
                <label for="password">Password</label>
                <input
                  v-model="password"
                  type="password"
                  class="form-control"
                  id="password"
                  placeholder="Enter your password"
                />
              </div>
              <button type="submit" class="btn btn-primary">Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
