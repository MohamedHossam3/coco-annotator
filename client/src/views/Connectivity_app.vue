<!-- src/views/NewFeature.vue -->
<template>
    <div>
        <h1>{{ title }}</h1>
        <p>Welcome to the Connectivity App page!</p>
    </div>
</template>

<script>
export default {
    name: "Connectivity_app",
    data() {
        return {
            title: 'Connectivity App'
        };
    }
};
</script>

<style scoped>
h1 {
    color: blue;
}
</style>
