---
Name: {{name}}
Race: {{race}}
Sex: {{caste}}
Birth Year: {{birth_year}}
Death: {{death_year}}
Historical Figure Number: {{id}}
---
# {{name}}
Race: {{race}}
Sex: {{caste}}
Birth Year: {{birth_year}}
Death: {{death_year}}
Job: {{associated_type}}
ID: [[hfid{{id}}]]

## Goals
{{goal}}. 

{{#if intrigue_plot}}Plot: {{#each intrigue_plot}}{{this.type}}, {{/each}}{{/if}}
## Skills
{{#each hf_skill}}
{{this.skill}}: {{this.total_ip}}
{{/each}}

## Sites

#site{{site_link.site_id}}

## Relationships
{{#each hf_link}}
**Relation:** {{this.link_type}}
 **hfid** [[hfid{{this.hfid}}]]
{{/each}}

## Entity Links
{{#each entity_link}}
**Status**: {{this.link_type}}
**Entity ID:** [[eid{{this.entity_id}}]]
**Link Strength**: {{this.link_strength}}
{{/each}}