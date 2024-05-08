<template>
    <div class="garage-item-grid">
        <div class="garage-name">
            <span class="name">{{ garage.name }}</span>
            <button @click="refresh">Refresh</button>
            <template v-if="!editing">
                <button type="button" class="btn btn-primary" @click="editing=!editing">Edit</button>
                <button type="button" class="btn btn-danger" @click="deleteGarage">Delete</button>
            </template>
            <template v-else>
                <!--<button type="button" class="btn btn-primary" @click="save">Save</button>-->
                <button type="button" class="btn btn-default" @click="editing=!editing; Object.assign(garage, updated_garage)">Cancel</button>
            </template>
        </div>
        <div v-if="editing" class="edit-garage">
            <garage-form :garage="garage" @change="editing = false; Object.assign(updated_garage, garage)"></garage-form>
        </div>
    </div>
</template>

<script>
    import GarageForm from "./garage-form";
    export default {
        name: "garage-list-item",
        components: {GarageForm},
        props: {
            garage: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                updated_garage: {},
                editing: false
            }
        },
        mounted() {
            this.updated_garage = Object.assign({}, this.garage);
        },
        methods: {
            deleteGarage() {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/garages/`,
                    data: JSON.stringify({'garage': this.garage.id})
                }).then((data) => {
                    this.$emit('change', data)
                }).always(() => {
                })
            },
            refresh() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/?garage=${this.garage.id}`,
                }).then((data) => {
                    console.log(data)
                    Object.assign(this.garage, data);
                    this.updated_garage = Object.assign({}, this.garage);
                }).always(() => {
                })
            }
        },
        watch: {
            garage(newVal) {
                // Update updated_garage when garage changes
                this.updated_garage = Object.assign({}, newVal);
            }
        }
    }
</script>

<style scoped>
    .garage-item-grid {
		display: grid;
		grid-template-columns: 1fr 3fr;
		grid-gap: 10px;
		grid-auto-rows: min-content;
		grid-template-areas:
			"garage-name edit-garage";
	}

    .garage-name {
        grid-area: garage-name;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 3fr 1fr;
        grid-auto-rows: min-content;
        grid-template-areas:
            "name btn-top"
            ". btn-bottom";
    }

    .btn-primary { grid-area: btn-top }
    .btn-default { grid-area: btn-bottom }
    .btn-danger { grid-area: btn-bottom }

    .edit-garage {
        grid-area: edit-garage;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 6fr 1fr;
        grid-template-areas:
            "name v-model-name"
            "brand v-model-brand"
            "country v-model-country";
        /* for some reason justify-items isn't working properly yet... */
        justify-items: end | start;
    }

    .name { grid-area: name; }
    .v-model-name { grid-area: v-model-name; }
    .brand { grid-area: brand; }
    .v-model-brand { grid-area: v-model-brand; }
    .country { grid-area: country; }
    .v-model-country {grid-area: v-model-country; }

</style>
