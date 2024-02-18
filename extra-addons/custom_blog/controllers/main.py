from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL

class BlogController(http.Controller):
    _blog_post_per_page = 20
    @http.route('/blog', type='http', auth='user', website=True)
    def blog(self, page=1):
        # Obtiene la compañía del usuario actual
        company_id = request.env.user.company_id.id
        
        # Filtra los blogs por la compañía del usuario actual y descendientes
        blogs = request.env['blog.blog'].search([('company_id', 'child_of', company_id)])
        
        # Obtiene las publicaciones asociadas a los blogs
        posts = request.env['blog.post'].search([('blog_id', 'in', blogs.ids)])
        
        #Obtiene el dominio
        domain = request.website.website_domain()
        
        #Obtiene el numero de publicaciones del dominio
        BlogPost = request.env['blog.post']
        total = BlogPost.search_count(domain)
        
        #rea un paginador para poder pasarselo a la vista
        pager = request.website.pager(
            url='/blog',
            total=total,
            page=page,
            step=self._blog_post_per_page,
        )
        
        blog_url = QueryURL('', ['blog',])
        
        # Renderiza la vista con los blogs y las publicaciones
        return http.request.render('website_blog.latest_blogs', {'posts': posts,
            'pager': pager,
            'blog_url': blog_url,})