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
						{ label: 'Phase 1 · Discovery', slug: 'guides/discovery' },
						{ label: 'Phase 2 · Production', slug: 'guides/production' },
						{ label: 'Phase 3 · Review', slug: 'guides/review' },
						{ label: 'Configuration', slug: 'guides/configuration' },
						{ label: 'Known Limitations', slug: 'guides/limitations' },
					],
				},
				{
					label: 'Skills',
					items: [
						{ label: 'All skills', slug: 'skills/overview' },
						{ label: 'Discovery', slug: 'skills/discovery' },
						{ label: 'Ideation & Drafting', slug: 'skills/ideation-drafting' },
						{ label: 'Refine & Repurpose', slug: 'skills/refine-repurpose' },
						{ label: 'German Workflow', slug: 'skills/german' },
					],
				},
			],
		}),
	],
});
