<script setup lang="ts">
import { onMounted } from 'vue';
import { usePostStore } from '@/stores';

const store = usePostStore();

onMounted(async () => {
  await store.getQueryGenres();
});

const genreChange = async (event: Event) => {
  const genreName = (event.target as HTMLSelectElement).value;
  await store.getQueryPosts(genreName);
};
</script>

<template>
  <select name="genres" id="id_genres" class="form-select" @change="genreChange">
    <option value="" selected disabled>Выберите жанр</option>
    <option v-for="genre in store.genres" :value="genre.name">{{ genre.name }}</option>
  </select>
  <div v-for="genre in store.genres" :key="genre.id">
    {{ genre.name }}
  </div>
</template>
