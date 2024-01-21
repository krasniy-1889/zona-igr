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
