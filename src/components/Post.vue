<script setup lang="ts">
import type { IPost } from '@/stores/types/post.types';

defineProps({
  post: {
    type: Object as () => IPost,
    required: true,
  },
});
</script>

<template>
  <div class="col-6 col-sm-4 col-md-3 col-lg-2 p-1">
    <div class="card">
      <img
        src="https://remanga.org/media/titles/necromancer-i-am-the-disaster/6df09f7fefa4128f89516254b7fd60ce.jpg"
        class="card-img-top"
        alt="..."
      />
      <div class="card-body">
        <h5 class="card-subtitle">
          <router-link :to="{ name: 'post-detail', params: { slug: post.slug } }">
            {{ post.title }}
          </router-link>
        </h5>
      </div>
    </div>
  </div>
</template>
