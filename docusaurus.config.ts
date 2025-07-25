import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Watchman',
  favicon: 'img/icon96.png',

  url: 'https://sofialctv.github.io',
  baseUrl: '/watchman-documentation/',

  projectName: 'watchman-documentation', // Usually your repo name.
  //deploymentBranch:"main",
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  markdown: {
    mermaid: true,
  
  },
  themes: ['@docusaurus/theme-mermaid'],

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  staticDirectories: ['static'],

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
          sidebarId: 'dsm',
          position: 'left',
          label: 'DSM',
        },
        {
          type: 'docSidebar',
          sidebarId: 'feedback',
          position: 'left',
          label: 'Feedback',
        },
        {
          type: 'docSidebar',
          sidebarId: 'gestao',
          position: 'left',
          label: 'Gestão',
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
          type: 'docSidebar',
          sidebarId: 'resultados',
          position: 'left',
          label: 'Resultados Finais',
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
