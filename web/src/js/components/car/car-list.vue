<template>
    <div class="grid-container">
      <div class="title">
        <h1>Cars</h1>
        <car-form :garageId="garageId" @changeCar="addCarToList"></car-form>
      </div>
      <div class="car-list-container">
        <ul class="list-group">
          <li v-for="car in carList" :key="car.id" class="list-group-item">
            <car-list-item :garageId="garageId" :car="car.car" @deleteCar="deleteCarFromList"></car-list-item>
          </li>
        </ul>
      </div>
    </div>
  </template>

<script>
    import CarListItem from "./car-list-item";
    import CarForm from "./car-form";

    export default {
        name: 'car-list',
        components: { CarForm, CarListItem },
        props: {
            garageId: {
                type: [String, Number],
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
					this.carList = data
				}).always(() => {
					this.loading = false
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

  .car-list-container {
    grid-area: car-list;
    max-height: 300px; /* Set a fixed height */
    overflow-y: auto; /* Enable vertical scrolling */
  }

  .list-group {
    padding: 0; /* Remove default padding */
    margin: 0; /* Remove default margin */
  }

  .list-group-item {
    list-style: none; /* Remove default list style */
  }
</style>