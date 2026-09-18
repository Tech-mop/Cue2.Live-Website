---
layout: default
t_ns: about
permalink: /about/
---

<div class="page about">
    <h1>{% t about.h1 %}</h1>
    <p>{% t about.intro %}</p>

    <h2>{% t about.project_h2 %}</h2>
    <p>{% t about.project_p %}</p>

    <h2>{% t about.license_h2 %}</h2>
    <p>{% t about.license_p1 %}</p>
    <p>{% t about.license_p2 %} <a href="https://docs.cue2.live/getting-started/licensing">{% t about.license_link %}</a>.</p>

    <h2>{% t about.links_h2 %}</h2>
    <ul>
        <li><a href="{% if site.active_lang == site.default_lang %}/{% else %}/{{ site.active_lang }}/{% endif %}#download">{% t about.download_cue2 %}</a></li>
        <li><a href="https://docs.cue2.live">{% t about.documentation %}</a></li>
        <li><a href="https://github.com/Tech-mop/Cue2">{% t about.app_source %}</a></li>
        <li><a href="https://github.com/Tech-mop/Cue2/issues">{% t about.issues %}</a></li>
        <li><a href="https://github.com/Tech-mop/Cue2.Live-Website">{% t about.website_source %}</a></li>
        <li><a href="https://github.com/Tech-mop/Docs.Cue2.Live">{% t about.docs_source %}</a></li>
    </ul>
</div>
