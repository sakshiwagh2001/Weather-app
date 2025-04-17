from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer

def weather_table_view(request):
    # Get filter parameters from request
    region = request.GET.get('region', '')
    parameter = request.GET.get('parameter', '')
    download = request.GET.get('download', '')
    
    # Filter records based on parameters
    records = WeatherRecord.objects.all()
    
    if region:
        records = records.filter(region=region)
    if parameter:
        records = records.filter(parameter=parameter)
    
    # Handle download request
    if download:
        return generate_txt_file(records, region, parameter)
    
    # Get unique regions and parameters for dropdowns
    regions = WeatherRecord.objects.values_list('region', flat=True).distinct()
    parameters = WeatherRecord.objects.values_list('parameter', flat=True).distinct()
    
    return render(request, 'weather_data/weather_list.html', {
        'records': records,
        'regions': regions,
        'parameters': parameters,
        'selected_region': region,
        'selected_parameter': parameter
    })

def generate_txt_file(records, region, parameter):
    # Create header similar to Met Office format
    header = f"UK Regional {parameter} data for {region}\n\n" if region and parameter else "UK Regional Weather Data\n\n"
    header += "Year   Jan    Feb    Mar    Apr    May    Jun    Jul    Aug    Sep    Oct    Nov    Dec    Annual\n"
    
    # Create data lines
    data_lines = []
    for record in records.order_by('year'):
        line = f"{record.year}  "
        line += f"{record.jan:6.1f}" if record.jan is not None else "    --"
        line += f"{record.feb:6.1f}" if record.feb is not None else "    --"
        line += f"{record.mar:6.1f}" if record.mar is not None else "    --"
        line += f"{record.apr:6.1f}" if record.apr is not None else "    --"
        line += f"{record.may:6.1f}" if record.may is not None else "    --"
        line += f"{record.jun:6.1f}" if record.jun is not None else "    --"
        line += f"{record.jul:6.1f}" if record.jul is not None else "    --"
        line += f"{record.aug:6.1f}" if record.aug is not None else "    --"
        line += f"{record.sep:6.1f}" if record.sep is not None else "    --"
        line += f"{record.oct:6.1f}" if record.oct is not None else "    --"
        line += f"{record.nov:6.1f}" if record.nov is not None else "    --"
        line += f"{record.dec:6.1f}" if record.dec is not None else "    --"
        line += f"{record.annual:6.1f}" if record.annual is not None else "    --"
        data_lines.append(line)
    
    # Combine header and data
    content = header + "\n".join(data_lines)
    
    # Create response
    response = HttpResponse(content, content_type='text/plain')
    filename = f"{parameter}_{region}.txt" if region and parameter else "weather_data.txt"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

class WeatherRecordViewSet(viewsets.ModelViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer

