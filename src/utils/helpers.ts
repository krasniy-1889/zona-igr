export function getPageFromUrl(url: string): string | null {
  if (!url) return null;
  return new URLSearchParams(new URL(url).search).get('page');
}
