import { getPageFromUrl } from '@/utils/helpers';
import axios from 'axios';
import { defineStore } from 'pinia';
import type { IGenre, IPagination, IPost } from '@/stores/types/post.types';

export const usePostStore = defineStore('posts', {
  state: () => ({
    posts: [] as IPost[],
    post: {} as IPost,
    genres: [] as IGenre[],
    error: false as boolean,
    pagination: {
      nextPage: '1',
    } as IPagination,
  }),
  actions: {
    async getQueryPosts(genre?: string) {
      if (!this.pagination.nextPage) {
        this.error = true;
        return;
      }

      const params = {} as any;
      params.page = this.pagination.nextPage;

      if (genre) {
        params.genre = genre;
      }

      const { data } = await axios.get('/posts', { params });
      const { results, next } = data;
      this.pagination.nextPage = getPageFromUrl(next) ?? null;
      this.posts.push(...results);
    },
    async getQueryPostBySlug(slug: string) {
      const { data } = await axios.get(`/posts/${slug}`);
      this.post = data;
    },
    async getQueryGenres() {
      const { data } = await axios.get('/genres/');
      this.genres = data.results;
    },
  },
  getters: {
    getPosts: (state) => state.posts,
  },
});
