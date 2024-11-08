from flask import jsonify
from flask_login import login_required
from flask_restplus import Namespace, Resource
import folium

api = Namespace('map', description='map related operations')


@api.route("/")
class Map(Resource):

    # @login_required
    # def get(self):
    #     """Extract map components and return them as JSON for Vue."""
    #     m = folium.Map(
    #         width=1024,
    #         height=600,
    #     )
    #     m.get_root().render()
    #     header = m.get_root().header.render()
    #     body_html = m.get_root().html.render()
    #     script = m.get_root().script.render()

    #     return jsonify({
    #         "header": header,
    #         "body_html": body_html,
    #         "script": script
    #     })

    @login_required
    def get(self):
        """Extract map components and return them as JSON for Vue."""
        m = folium.Map(width=1024, height=600, location=[50.624889, 6.989990], zoom_start=19)

        url = "https://leafletjs.com/examples/custom-icons/{}".format
        icon_image = url("leaf-red.png")
        shadow_image = url("leaf-shadow.png")

        icon = folium.CustomIcon(
            icon_image,
            icon_size=(38, 95),
            icon_anchor=(22, 94),
            shadow_image=shadow_image,
            shadow_size=(50, 64),
            shadow_anchor=(4, 62),
            popup_anchor=(-3, -76),
        )

        folium.Marker(
            location=[50.624889, 6.989990], icon=icon, popup="Weed..FIRE"
        ).add_to(m)

        m.get_root().render()
        header = m.get_root().header.render()
        body_html = m.get_root().html.render()
        script = m.get_root().script.render()

        return jsonify({
            "header": header,
            "body_html": body_html,
            "script": script
        })
