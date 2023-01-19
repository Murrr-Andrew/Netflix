from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', )


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft', )
    actions = ['publish', 'unpublish']

    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': (('description', 'poster'), )
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'), )
        }),
        ('Actors', {
            'classes': ('collapse', ),
            'fields': (('actors', 'producers', 'genres', 'category'), )
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'), )
        }),
        ('Options', {
            'fields': (('slug', 'draft'), )
        })
    )

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = '1 post was updated'
        else:
            message_bit = f'{row_update} posts were updated'

        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = '1 post was updated'
        else:
            message_bit = f'{row_update} posts were updated'

        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change', )

    unpublish.short_description = 'Unpublish'
    unpublish.allowed_permissions = ('change',)



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60" />')

    get_image.short_description = 'Image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')


admin.site.register(RatingStar)
