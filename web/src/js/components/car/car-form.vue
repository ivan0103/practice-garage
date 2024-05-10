<template>
    <div>
        <h3>{{title}}</h3>
        <div class="row">
            <label class="col-sm-4">Plate</label>
            <input type="text" class="col-sm-8" v-model="myCar.plate"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Brand</label>
            <input type="text" class="col-sm-8" v-model="myCar.brand"/>
        </div>
        <div class="row">
            <button class="pull-right btn btn-success" @click="add">Add</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "new-car",
        props: {
            garageId: {
                type: [Number,String],
                required: true
            },
            car: {
                type: Object,
                required: false,
                default: null
            }
        },
        computed: {
            title(){
                return this.car ? 'Edit car' : 'Add new car';
            }
        },
        data() {
            return {
                myCar: {
                    plate: '',
                    brand: '',
                }
            }
        },
        mounted() {
            Object.assign(this.myCar, this.car);
        },
        methods: {
            add() {
                const method = this.car ? 'PUT' : 'POST';
                $.ajax({
                    type: method,
                    url: `/garages/${this.garageId}/cars`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.myCar),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('changeCar', data)
                    if (this.car){
                        this.resetCarForm()
                    }
                }).always(() => {
                    this.loading = false;
                })
            },
            resetCarForm() {
                if (this.car) {
                    Object.assign(this.car, this.myCar);
                } else {
                    this.myCar = {
                        plate: '',
                        brand: ''
                    };
                }
            }
        },
    }
</script>

<style scoped>

</style>