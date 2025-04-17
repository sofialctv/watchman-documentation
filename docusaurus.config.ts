import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Watchman',
  favicon: 'img/icon96.png',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Watchman',
      logo: {
        src: 'img/icon96.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'backlog',
          position: 'left',
          label: 'Backlog',
        },
        {
          type: 'docSidebar',
          sidebarId: 'comunicacao',
          position: 'left',
          label: 'Comunicação',
        },
        {
          type: 'docSidebar',
          sidebarId: 'disc',
          position: 'left',
          label: 'DISC',
        },
        {
          type: 'docSidebar',
          sidebarId: 'feedback',
          position: 'left',
          label: 'Feedback',
        },
        {
          type: 'docSidebar',
          sidebarId: 'metricas',
          position: 'left',
          label: 'Métricas',
        },
        {
          type: 'docSidebar',
          sidebarId: 'pmc',
          position: 'left',
          label: 'PMC',
        },
        {
          type: 'docSidebar',
          sidebarId: 'team_topology',
          position: 'left',
          label: 'Team Topology',
        },
        {
          type: 'dropdown',
          label: 'Links',
          position: 'right',
          items: [
            {
              label: 'GitHub Projects',
              href: 'https://github.com/users/joaomrpimentel/projects/1',
            },
            {
              label: 'Código Fonte',
              href: 'https://github.com/joaomrpimentel/watchman',
            },
            {
              label: 'Código Fonte - Documentação',
              href: 'https://github.com/sofialctv/watchman-documentation',
            },
          ],
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
