from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    FileField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    URLField,
)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


class Tag(Model):
    """Labels to help categorize data"""

    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Tag"""
        return reverse(
            "tag_detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        """Return URL to update page of Tag"""
        return reverse(
            "tag_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Tag"""
        return reverse(
            "tag_delete", kwargs={"slug": self.slug}
        )


class Startup(Model):
    """Data about a Startup company"""

    name = CharField(max_length=31, db_index=True)
    slug = AutoSlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config.",
        populate_from=["name"]
    )
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#filefield
    description = TextField()
    founded_date = DateField("date founded")
    website = URLField(
        max_length=255  # https://tools.ietf.org/html/rfc3986
    )
    tags = ManyToManyField(Tag)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "startup_detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        """Return URL to update page of Startup"""
        return reverse(
            "startup_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Startup"""
        return reverse(
            "startup_delete", kwargs={"slug": self.slug}
        )

    def get_newslink_create_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "newslink_create",
            kwargs={"startup_slug": self.slug},
        )


class NewsLink(Model):
    """Link to external sources about a Startup"""

    title = CharField(max_length=63)
    slug = AutoSlugField(max_length=63,unique=True, populate_from=["title"])
    pub_date = DateField("date published")
    link = URLField(
        max_length=255  # https://tools.ietf.org/html/rfc3986
    )
    startup = ForeignKey(Startup, on_delete=CASCADE)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "startup")
        verbose_name = "news article"

    def __str__(self):
        return f"{self.startup}: {self.title}"

    def get_absolute_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "startup_detail",
            kwargs={"slug": self.startup.slug},
        )

    def get_update_url(self):
        """Return URL to update page of Startup"""
        return reverse(
            "newslink_update",
            kwargs={
                "startup_slug": self.startup.slug,
                "newslink_slug": self.slug,
            },
        )

    def get_delete_url(self):
        """Return URL to delete page of Startup"""
        return reverse(
            "newslink_delete",
            kwargs={
                "startup_slug": self.startup.slug,
                "newslink_slug": self.slug,
            },
        )