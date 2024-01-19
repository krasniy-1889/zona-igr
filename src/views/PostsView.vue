<script lang="ts" setup>
import { usePostStore } from '@/stores';
import { getCookie } from '@/utils/cookies';
import { computed, onMounted, ref } from 'vue';

const store = usePostStore();
const search = ref<string>('');

const loadMore = async () => {
  await store.getQueryPosts();
};

onMounted(async () => {
  await store.getQueryPosts();
});

const sorted_posts = computed(() => {
  if (search.value === '') {
    return store.posts;
  }
  return store.posts.filter((post) => post.slug.includes(search.value));
});
</script>

<template>
  <div class="container">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Slug</th>
          <th scope="col">Likes</th>
          <th scope="col">Dislikes</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in sorted_posts" :key="post.id">
          <td>
            {{ post.id }}
          </td>
          <td>
            {{ post.slug }}
          </td>
          <td>
            {{ post.likes_count }}
          </td>
          <td>
            {{ post.dislikes_count }}
          </td>
          <td>
            <div class="btn-group">
              <button type="button" class="btn btn-info">Edit</button>
              <button type="button" class="btn btn-danger">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
