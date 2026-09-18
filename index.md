---
layout: default
t_ns: home
permalink: /
---

<div class="hero-text">
    <h1>{% t home.hero_h1 %}</h1>
    <p class="lede">{% t home.hero_lede %}</p>
</div>
<header>
    <img src="{{ '/assets/img/Cue2v0.1_Window.PNG' | relative_url }}" alt="{% t home.screenshot_alt %}" width="800" height="526">
</header>
{% include download.html %}

<div class="page">
    <p class="release-note">{% t home.release_note %}</p>

    <h2>{% t home.about_h2 %}</h2>
    <p>{% t home.about_p1 %}</p>
    <p>{% t home.about_p2 %}</p>

    <h2>{% t home.features_h2 %}</h2>
    <ul class="features">
        <li>
            <h3>{% t home.feature_audio_h3 %}</h3>
            <p>{% t home.feature_audio_p %} <a href="https://docs.cue2.live/tutorials/zero-to-audio">{% t home.feature_audio_link %}</a></p>
        </li>
        <li>
            <h3>{% t home.feature_video_h3 %}</h3>
            <p>{% t home.feature_video_p %} <a href="https://docs.cue2.live/tutorials/zero-to-video">{% t home.feature_video_link %}</a></p>
        </li>
        <li>
            <h3>{% t home.feature_show_h3 %}</h3>
            <p>{% t home.feature_show_p %} <a href="https://docs.cue2.live/networking/osc-command-reference">{% t home.feature_show_link %}</a></p>
        </li>
        <li>
            <h3>{% t home.feature_seq_h3 %}</h3>
            <p>{% t home.feature_seq_p %} <a href="https://docs.cue2.live/fundamentals/cue-sequences">{% t home.feature_seq_link %}</a></p>
        </li>
        <li>
            <h3>{% t home.feature_cross_h3 %}</h3>
            <p>{% t home.feature_cross_p %} <a href="https://docs.cue2.live/getting-started/system-requirements">{% t home.feature_cross_link %}</a></p>
        </li>
        <li>
            <h3>{% t home.feature_oss_h3 %}</h3>
            <p>{% t home.feature_oss_p %} <a href="https://docs.cue2.live/getting-started/licensing">{% t home.feature_oss_link %}</a></p>
        </li>
    </ul>

    <h2>{% t home.who_h2 %}</h2>
    <p>{% t home.who_p1 %}</p>
    <p>{% t home.who_p2 %}</p>

    <h2>{% t home.start_h2 %}</h2>
    <ol class="start-list">
        <li><a href="https://docs.cue2.live/getting-started/install">{% t home.start_install %}</a></li>
        <li><a href="https://docs.cue2.live/getting-started/concepts">{% t home.start_concepts %}</a></li>
        <li><a href="https://docs.cue2.live/tutorials/zero-to-audio">{% t home.start_audio %}</a></li>
        <li><a href="https://docs.cue2.live/networking/osc-command-reference">{% t home.start_osc %}</a></li>
    </ol>
    <p>{% t home.start_manual %} <a href="https://docs.cue2.live">docs.cue2.live</a>.</p>
</div>
