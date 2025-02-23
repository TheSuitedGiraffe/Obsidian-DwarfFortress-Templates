{{#if (eq type "hf simple battle event")}}
# Simple Battle @ #siteid{{site_id}}
[[hfid{{group_1_hfid}}]] attacked [[hfid{{group_2_hfid}}]] in {{year}}
{{#if subtype}}
{{subtype}}
{{/if}}
{{/if}}

{{#if (eq type "written content composed")}}
# Written content @ #siteid{{site_id}}
[[hfid{{hist_figure_id}}]] wrote in {{year}} {{#if circumstance}} because of {{circumstance}}{{/if}}. {{#if reason}}They want to {{reason}}. {{/if}}
{{/if}}