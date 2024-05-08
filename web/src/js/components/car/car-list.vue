<template>
    <div class="grid-container">
        <div class="title">
            <h1>Cars</h1>
            <new-car :garageId="garageId.toString()"></new-car>
        </div>
        <ul class="list-group">
            <li v-for="car in carList" :key="car.id" class="list-group-item">
                <car-list-item :garageId="garageId" :car="car"></car-list-item>
            </li>
        </ul>
    </div>
</template>

<script>
    import CarListItem from "./car-list-item";
    import NewCar from "./new-car";

    export default {
        name: 'car-list',
        components: { NewCar, CarListItem },
        props: {
            garageId: {
                type: [String, Number], // Accepts both string and number
                required: true
            }
        },
        data() {
            return {
                carList: [],
            }
        },
        methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/garages/${this.garageId}/cars`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					console.log(data)
					this.carList = data
				}).always(() => {
					// this.loading = false
				})
			},
			addCarToList(newCar) {
                this.carList.push(newCar)
            },
			deleteCarFromList(carId) {
				const index = this.carList.findIndex(item => item.car.id === carId);
				if (index !== -1) {
					this.carList.splice(index, 1);
				}
			},
        },
        created() {
            // Load car data when the component is created
            this.load();
        }
    }
</script>

<style scoped>
    .grid-container {
        display: grid;
        grid-template-columns: 2fr 6fr;
        grid-gap: 10px;
        grid-auto-rows: min-content;
        grid-template-areas: "title car-list ";
    }

    .title {
        grid-area: title;
        margin-right: 20px;
    }

    .list-group {
        grid-area: car-list;
    }

    .add-car {
        margin: 4px;
    }
</style>
