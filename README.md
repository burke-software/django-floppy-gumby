django-floppy-gumby
===================

![ScreenShot](/images/screen.png)

# Setup

1. pip install django-floppy-gumby`
1. Add `'floppy_gumby_forms',` to INSTALLED_APPS before floppyforms
1. Set up [django-floppy-forms](http://django-floppyforms.readthedocs.org/)

# Usage

Read up and have a basic understanding of floppyforms first. Note you need to import floppyforms.forms for
anything to work. Also note floppy forms requires explicitly stating the widgets in ModelForms.

Use floppy_gumby form templates as desired. For example

```
{% load floppyforms %}
{% form my_form using "floppy_gumby_forms/layouts/gumby.html" %}
```

You may also use single rows like this

```
{% form form %}
{% formconfig row using "floppy_gumby_forms/rows/gumby.html" %}
{% formrow form.prefered_file_format %}
{% endform %}
```

You may want to extend floppy_forms. If you add features make sure to send a pull request :)

It would also be nice to eventually multiple styles. For example forms with placeholder text instead of labels.
