<template>
  <div>
    <!-- Map and Video Stream Layout -->
    <div class="content-container">
      <!-- Map Section -->
      <div v-html="header" />
      <div id="map-container" v-html="bodyHtml" />
    
      <!-- Video Stream Section -->
      <div id="video-container">
        <img :src="streamUrl" alt="Robot Camera Stream" />
        <h2>Robot Camera Stream</h2>
      </div>
    </div>

      
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
      rosHost: "localhost",  // IP of the ROS 2 web video server
      port: 8090,            // Port of the ROS 2 web video server
      topic: "/camera/image_raw",  // ROS 2 image topic name
    };
  },
  computed: {
    // Construct the stream URL for the ROS 2 web video server
    streamUrl() {
      return `http://${this.rosHost}:${this.port}/stream?topic=${this.topic}`;
    },
  },
  mounted() {
    this.fetchMapComponents();
  },
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
/* Container for the map and video stream */
.content-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

/* Map Container */
#map-container {
  width: 100%;
  max-width: 800px;
  height: 600px;
}

/* Video Container */
#video-container {
  width: 100%;
  max-width: 800px;
  height: 600px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#video-container img {
  width: 100%;
  height: auto;
  background-color: black;
  object-fit: cover;
}
</style>