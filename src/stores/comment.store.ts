import { defineStore } from 'pinia';

export const useCommentStore = defineStore('comments', {
  state: () => ({
    comments: [],
  }),
  actions: {},
});
