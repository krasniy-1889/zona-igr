<script lang="ts" setup>
import { useAuthStore } from '@/stores';

import { ref } from 'vue';

const store = useAuthStore();
const username = ref<string>('');
const email = ref<string>('');
const password = ref<string>('');

const register = async () => {
  await store.register(username.value, email.value, password.value);
};
</script>

<template>
  <div
    id="hs-register-modal"
    class="hs-overlay hidden w-full h-full fixed top-0 start-0 z-[80] overflow-x-hidden overflow-y-auto pointer-events-none"
  >
    <div
      class="hs-overlay-open:mt-7 hs-overlay-open:opacity-100 hs-overlay-open:duration-500 mt-0 opacity-0 ease-out transition-all sm:max-w-lg sm:w-full m-3 sm:mx-auto"
    >
      <div
        class="flex flex-col bg-white border shadow-sm rounded-xl pointer-events-auto dark:bg-gray-800 dark:border-gray-700 dark:shadow-slate-700/[.7]"
      >
        <div class="flex justify-between items-center py-3 px-4 border-b dark:border-gray-700">
          <h3 class="font-bold text-gray-800 dark:text-white">Register</h3>
          <button
            type="button"
            class="flex justify-center items-center w-7 h-7 text-sm font-semibold rounded-full border border-transparent text-gray-800 hover:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:hover:bg-gray-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            data-hs-overlay="#hs-register-modal"
          >
            <span class="sr-only">Close</span>
            <svg
              class="flex-shrink-0 w-4 h-4"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M18 6 6 18" />
              <path d="m6 6 12 12" />
            </svg>
          </button>
        </div>
        <form class="flex-col flex" @submit.prevent="register">
          <div class="p-4 overflow-y-auto">
            <label for="input-label" class="block text-sm font-medium mb-2 dark:text-white">Username</label>
            <input
              v-model="username"
              type="text"
              id="input-label"
              class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
              placeholder="Username..."
              autofocus
            />
          </div>
          <div class="p-4 overflow-y-auto">
            <label for="input-label" class="block text-sm font-medium mb-2 dark:text-white">Email</label>
            <input
              v-model="email"
              type="email"
              id="input-label"
              class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
              placeholder="Email..."
              autofocus
            />
          </div>
          <div class="p-4 overflow-y-auto">
            <label for="input-label" class="block text-sm font-medium mb-2 dark:text-white">Password</label>
            <input
              v-model="password"
              type="password"
              id="input-label"
              class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
              placeholder="Password"
              autofocus
            />
          </div>
          <div class="flex justify-end items-center gap-x-2 py-3 px-4 border-t dark:border-gray-700">
            <button
              type="submit"
              class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-white dark:hover:bg-gray-800 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
              data-hs-overlay="#hs-focus-management-modal"
            >
              Close
            </button>
            <button
              @click="register"
              type="button"
              class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
            >
              Register
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
