import { defineStore } from 'pinia';
import type { IGenre, IPagination, IPost } from '@/stores/types/post.types';
import { $api } from '@/api';

export const usePostStore = defineStore('posts', {
  state: () => ({
    posts: [] as IPost[],
    post: {} as IPost,
    genres: [] as IGenre[],
    error: false as boolean,
    queryParams: {} as any,
    pagination: {
      currentPage: 1,
      hasNextPage: true,
    } as IPagination,
  }),
  actions: {
    async getQueryPosts(genre?: string) {
      if (!this.pagination.hasNextPage) {
        this.error = true;
        return;
      }
      const params = {} as any;

      params.page = this.pagination.currentPage;

      if (genre) {
        params.genre = genre;
      }

      const { data } = await $api.get('/posts', { params });
      const { results, next } = data;
      if (next) {
        this.pagination.hasNextPage = true;
        this.pagination.currentPage++;
      } else {
        this.pagination.hasNextPage = false;
      }
      this.posts.push(...results);
    },

    async getQueryPostBySlug(slug: string) {
      const { data } = await $api.get(`/posts/${slug}`);
      this.post = data;
    },

    async getQueryGenres() {
      const { data } = await $api.get('/genres/');
      this.genres = data.results;
    },
  },
  getters: {
    getPosts: (state) => state.posts,
  },
});
