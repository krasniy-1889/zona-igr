import { getPageFromUrl } from '@/utils/helpers';
import axios from 'axios';
import { defineStore } from 'pinia';

export interface IPost {
  id: number;
  title: string;
  slug: string;
  poster: string;
  voiceover_language: string;
  interface_language: string;
  developer: number;
  content: string;
  operating_system: string;
  processor: string;
  memory: string;
  video_card: string;
  sound_card: string;
  disk_space: string;
  likes_count: number;
  dislikes_count: number;
  created_at: string;
  updated_at: string;
  comments_count: number;
  genres: IGenre[];
}

export interface IGenre {
  id: number;
  name: string;
}

export interface IPagination {
  nextPage: string | null;
  previousPage: string | null;
}

export const usePostStore = defineStore('posts', {
  state: () => ({
    posts: [] as IPost[],
    error: false as boolean,
    pagination: {
      nextPage: '1',
    } as IPagination,
  }),
  actions: {
    async getQueryPosts() {
      if (!this.pagination.nextPage) {
        this.error = true;
        return;
      }
      const { data } = await axios.get('/posts?page=' + this.pagination.nextPage);
      const { results, next } = data;
      this.pagination.nextPage = getPageFromUrl(next) ?? null;
      this.posts.push(...results);
    },
  },
  getters: {
    getPosts: (state) => state.posts,
  },
});
