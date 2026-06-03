// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	// GitHub Pages project site: served from https://donheidi.github.io/online-writing-skills/
	site: 'https://donheidi.github.io',
	base: '/online-writing-skills',
	integrations: [
		starlight({
			title: 'Online Writing',
			description:
				'A suite of AI-agent skills for social-first online writing: purpose and voice discovery, ideation, drafting, diagnostics, rating, and repurposing.',
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/DonHeidi/online-writing-skills',
				},
				{
					icon: 'external',
					label: 'sebastian-heitmann.dev',
					href: 'https://www.sebastian-heitmann.dev',
				},
			],
			editLink: {
				baseUrl: 'https://github.com/DonHeidi/online-writing-skills/edit/main/site/',
			},
			sidebar: [
				{
					label: 'Guides',
					items: [
						{ label: 'Overview', slug: 'index' },
						{ label: 'Installation', slug: 'guides/installation' },
						{ label: 'Getting Started', slug: 'guides/getting-started' },
						{ label: 'Configuration', slug: 'guides/configuration' },
						{ label: 'Known Limitations', slug: 'guides/limitations' },
					],
				},
				{
					label: 'Workflow',
					items: [
						{ label: 'Discovery', slug: 'guides/discovery' },
						{ label: 'Production', slug: 'guides/production' },
						{ label: 'Review', slug: 'guides/review' },
					],
				},
				{
					label: 'Skills',
					items: [
						{ label: 'All skills', slug: 'skills/overview' },
						{
							label: 'Discovery',
							items: [
								{ label: 'discover-purpose', slug: 'skills/discover-purpose' },
								{ label: 'discover-buckets', slug: 'skills/discover-buckets' },
								{ label: 'discover-tonality', slug: 'skills/discover-tonality' },
							],
						},
						{
							label: 'Ideation & Drafting',
							items: [
								{ label: 'ideate', slug: 'skills/ideate' },
								{ label: 'explore-idea', slug: 'skills/explore-idea' },
								{ label: 'create-post', slug: 'skills/create-post' },
								{ label: 'create-draft', slug: 'skills/create-draft' },
								{ label: 'create-medium-post', slug: 'skills/create-medium-post' },
								{ label: 'headlines', slug: 'skills/headlines' },
							],
						},
						{
							label: 'Refine & Repurpose',
							items: [
								{ label: 'improve-writing', slug: 'skills/improve-writing' },
								{ label: 'diagnose', slug: 'skills/diagnose' },
								{ label: 'rate', slug: 'skills/rate' },
								{ label: 'tldr', slug: 'skills/tldr' },
								{ label: 'distill', slug: 'skills/distill' },
								{ label: 'illustrate', slug: 'skills/illustrate' },
							],
						},
						{
							label: 'German Workflow',
							items: [
								{ label: 'finde-stil', slug: 'skills/finde-stil' },
								{ label: 'analysiere-quelle', slug: 'skills/analysiere-quelle' },
								{ label: 'schreibe-entwurf', slug: 'skills/schreibe-entwurf' },
								{ label: 'rewrite-de', slug: 'skills/rewrite-de' },
							],
						},
					],
				},
				{
					label: 'Legal',
					items: [
						{ label: 'Privacy', slug: 'legal/privacy' },
						{ label: 'Imprint', slug: 'legal/imprint' },
					],
				},
			],
		}),
	],
});
