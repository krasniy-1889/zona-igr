<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useAuthStore, usePostStore } from '@/stores';
import type { IPost } from '@/stores/types/post.types';
import { useRoute } from 'vue-router';

const store = usePostStore();

const route = useRoute();
const postSlug = route.params.slug as string;

onMounted(async () => {
  await store.getQueryPostBySlug(postSlug);
});
</script>

<template>
  {{ store.post.slug }}
</template>
