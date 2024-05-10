<template>
    <div>
        <h3>{{ title }}</h3>
        <div class="row">
            <label class="col-sm-4">Name</label>
            <input type="text" class="col-sm-8" v-model="myGarage.name"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Brand</label>
            <input type="text" class="col-sm-8" v-model="myGarage.brand"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Country</label>
            <input type="text" class="col-sm-8" v-model="myGarage.postal_country"/>
        </div>
        <div class="row">
            <button class="pull-right btn btn-success" @click="save">Save</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "garage-form",
        props: {
            garage: {
                type: Object,
                required: false,
                default: null
            }
        },
        computed: {
            title() {
                return this.garage ? 'Edit garage' : 'Add new garage';   
            }
        },
        data() {
            return {
                myGarage: {
                    name: '',
                    brand: '',
                    postal_country: ''
                }
            };
        },
        mounted() {
                Object.assign(this.myGarage, this.garage);
        },
        methods:{
            save() {
                const method = this.garage ? 'PUT' : 'POST';
                $.ajax({
                    type: method,
                    url: `/garages/`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.myGarage),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('change', data)
                    if (this.garage){
                        this.resetForm()
                    }
                }).always(() => {
                    this.loading = false;
                });
            },
            resetForm() {
                if (this.garage) {
                    Object.assign(this.garage, this.myGarage);
                } else {
                    this.myGarage = {
                        name: '',
                        brand: '',
                        postal_country: ''
                    };
                }
            }
        }
    }
</script>

<style scoped>

</style>
