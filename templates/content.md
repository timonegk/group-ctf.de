{% extends "base.html" %}

{% block content %}
<div id="markdown">
{{ md_text }}
</div>
{% endblock %}

{% block scripts %}
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/remarkable/2.0.1/remarkable.min.js"></script>
<script type="text/javascript">
(function() {
    const { Remarkable } = window.remarkable;
    const md = new Remarkable();
    const md_element = document.getElementById("markdown");
    const text = md_element.textContent;
    md_element.innerHTML = md.render(text);
})();
</script>
{% endblock %}
