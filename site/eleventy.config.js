export default function (eleventyConfig) {
  // Copy the stylesheet straight through to the output.
  eleventyConfig.addPassthroughCopy("src/css");

  // One collection per blog: dated posts only, newest first.
  // The about / comment-policy pages have no date and are excluded here;
  // they surface through the section nav instead.
  const datedPosts = (collectionApi, glob) =>
    collectionApi
      .getFilteredByGlob(glob)
      .filter((item) => Boolean(item.data.date))
      .sort((a, b) => new Date(b.data.date) - new Date(a.data.date));

  eleventyConfig.addCollection("life", (api) =>
    datedPosts(api, "src/life/*.md")
  );
  eleventyConfig.addCollection("tech", (api) =>
    datedPosts(api, "src/tech/*.md")
  );

  // Standalone (undated) pages within a section, for the footer nav.
  const pagesIn = (collectionApi, glob) =>
    collectionApi
      .getFilteredByGlob(glob)
      .filter((item) => !item.data.date)
      .sort((a, b) => (a.data.title || "").localeCompare(b.data.title || ""));

  eleventyConfig.addCollection("lifePages", (api) =>
    pagesIn(api, "src/life/*.md")
  );
  eleventyConfig.addCollection("techPages", (api) =>
    pagesIn(api, "src/tech/*.md")
  );

  // Year of a post's date, e.g. 2007. Used to group an archive.
  eleventyConfig.addFilter("year", (value) =>
    value ? new Date(value).getUTCFullYear() : ""
  );

  // Human-friendly date, e.g. "14 July 2007".
  eleventyConfig.addFilter("readableDate", (value) => {
    if (!value) return "";
    const d = new Date(value);
    return d.toLocaleDateString("en-GB", {
      day: "numeric",
      month: "long",
      year: "numeric",
      timeZone: "UTC",
    });
  });

  return {
    // GitHub Pages serves this project site under a subpath that matches the
    // repository name. The `url` filter applied to internal links honours this.
    // Override at build time with: npx @11ty/eleventy --pathprefix=/
    pathPrefix: "/suburbandestiny/",
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
}
