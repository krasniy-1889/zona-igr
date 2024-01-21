<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { useAuthStore, usePostStore } from '@/stores';
import Post from '@/components/Post.vue';
import GenresList from '@/components/post/GenresList.vue';

const store = usePostStore();

const loadMore = async () => {
  await store.getQueryPosts();
};

onMounted(async () => {
  if (store.getPosts.length === 0) {
    await store.getQueryPosts();
  }
});
</script>

<template>
  <div class="d-flex justify-content-between align-items-center">
    <div class="btn btn-success align-content-start" @click="loadMore">Load More</div>
    <div class="text-center font-weight-bold">
      Загружено постов: <span class="text-info">{{ store.posts.length }}</span>
    </div>
  </div>
  <div class="row justify-content-center mt-2">
    <div class="col-12 col-md-2">
      <GenresList />
    </div>
    <div class="row col">
      <Post v-for="post in store.posts" :key="post.id" :post="post" />
    </div>
  </div>
</template>
