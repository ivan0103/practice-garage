<template>
    <div class="car-item-grid">
        <div class="car-name">
            <span class="plate">{{ car.plate }}</span>
            <template v-if="!editing">
                <button type="button" class="btn btn-primary" @click="editing=!editing">Edit</button>
                <button type="button" class="btn btn-danger" @click="deleteCar">Delete</button>
            </template>
            <template v-else>
                <button type="button" class="btn btn-default" @click="editing=!editing; Object.assign(car, update_car)">Cancel</button>
            </template>
    	</div>
        <div v-if="editing" class="edit-car">
            <car-form></car-form>
        </div>
    </div>
</template>

<script>
    import CarForm from "./car-form";

    export default {
        name: "car-list-item",
        components: { CarForm },
        props: {
            car: {
                type: Object,
                required: true
            },
			garageId: {
                type: [String, Number], // Accepts both string and number
                required: true
            }
        },
        data() {
            return {
                updated_car: {},
                editing: false,
            }
        },
        mounted() {
            this.updated_car = Object.assign({}, this.car);
        },
        // methods: {
        //     deleteCar() {
        //         $.ajax({
        //             type: 'DELETE',
        //             contentType: 'application/json',
        //             url: `/garages/<this.garageId>/car`,
        //             data: JSON.stringify({ 'car': this.car.id })
        //         }).then((data) => {
        //             this.$emit('delete', this.car.id)
        //         }).always(() => {
        //         })
        //     },
        //     toggleCars() {
        //         this.cars = !this.cars;
        //     }
        // },
        // watch: {
        //     car(newVal) {
        //         // Update updated_car when car changes
        //         this.updated_car = Object.assign({}, newVal);
        //     }
        // }
    }
</script>

<style scoped>
    .car-item-grid {
        display: grid;
        grid-template-columns: 1fr 3fr;
        grid-gap: 10px;
        grid-auto-rows: min-content;
        grid-template-areas: "car-brand edit-car";
    }

    .car-name {
        grid-area: car-name;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 3fr 1fr;
        grid-auto-rows: min-content;
        grid-template-areas: "name btn-top" ". btn-bottom";
    }

    .btn-primary { grid-area: btn-top }
    .btn-default { grid-area: btn-bottom }
    .btn-danger { grid-area: btn-bottom }

    .edit-car {
        grid-area: edit-car;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 6fr 1fr;
        grid-template-areas: "brand v-model-brand" "brand v-model-brand" "country v-model-country";
        justify-items: end | start;
    }

    .name { grid-area: plate; }
    .v-model-plate { grid-area: v-model-plate; }
    .brand { grid-area: brand; }
    .v-model-brand { grid-area: v-model-brand; }
</style>