<template>
  <div>
    <!-- Add Leaflet CSS -->
    <!-- <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
    /> -->
    <div v-html="header" />
    <div id="map-container" v-html="bodyHtml" />
    <div>
      <h1>Alterdorf</h1>
    </div>
  </div>
</template>

<script>
import Map from "@/models/map";

export default {
  data() {
    return {
      header: "",      // To store the map's <head> content
      bodyHtml: "",    // To store the map's <body> content
      script: "",      // To store the map's <script> content
    };
  },
  mounted() {
    this.fetchMapComponents();
  },
  // methods: {
  //   fetchMapComponents() {
  //     try {
  //       const response = Map.getMap();
  //       this.header = response.data.header;
  //       this.bodyHtml = response.data.body_html;
  //       this.script = response.data.script;

  //       // Dynamically insert the script into the page
  //       const scriptElement = document.createElement("script");
  //       scriptElement.innerHTML = this.script;
  //       document.body.appendChild(scriptElement);
  //     } catch (error) {
  //       console.error("Failed to fetch map components:", error);
  //     }
  //   },
  // },
  methods: {
  async fetchMapComponents() {
    try {
      const response = await Map.getMap();
      this.header = response.data.header;
      this.bodyHtml = response.data.body_html;
      this.script = response.data.script;

      // Ensure Leaflet.js is loaded before injecting the map script
      if (!window.L) {
        const leafletScript = document.createElement("script");
        leafletScript.src = "https://unpkg.com/leaflet@1.7.1/dist/leaflet.js";
        leafletScript.onload = () => {
          this.appendMapScript();
        };
        document.head.appendChild(leafletScript);
      } else {
        this.appendMapScript();
      }
    } catch (error) {
      console.error("Failed to fetch map components:", error);
    }
  },
  appendMapScript() {
    const scriptElement = document.createElement("script");
    scriptElement.innerHTML = this.script;
    document.body.appendChild(scriptElement);
  },
},
};
</script>

<style scoped>
#map-container {
  width: 1024px;
  height: 600px;
}
</style>
